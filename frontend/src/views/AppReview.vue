

 <template>
  <SimpleComboBox ref="SimpleCombobox" @languageSelected="languageSelected"></SimpleComboBox>

	<div class="mt-4">
		<CardWithDetails
			title="Pending Applications"
			:show-details="selectedCandidate"
		>
			<div>
				<router-link
					v-for="candidate in candidates"
					class="block cursor-pointer rounded-md px-2.5"
					:class="
						selectedCandidate && selectedCandidate.name === candidate.name
							? 'bg-gray-100'
							: 'hover:bg-gray-50'
					"
					:key="candidate.name"
					:to="`/apps/${app_name}/review/${candidate.name}`"
				>
					<ListItem
						:title="` ${candidate.source_message}, translated to
							${candidate.translated}
						`"
						:subtitle="candidate.name"
					>
						<template #actions>
							<Badge

								:status="candidate.status"
							>
								{{ candidate.status }}
							</Badge>
						</template>
					</ListItem>
					<div class="border-b"></div>
				</router-link>
				<div class="py-3" v-if="!$resources.candidates.lastPageEmpty">
					<Button
						:loading="$resources.candidates.loading"
						loadingText="Loading..."
						@click="pageStart += 10"
					>
						Load more
					</Button>
				</div>
			</div>
			<template #details>
				<TranslatedMessageDetail
					:showDetails="selectedCandidate"
					:loading="$resources.selectedCandidate.loading"
					title="Translated Message Details"
					@translatedMessageManaged="translatedMessageManaged"
				/>
			</template>
		</CardWithDetails>
	</div>
</template>

<script>
import { Button, Alert, Card } from "frappe-ui";
import {  ref } from 'vue'
import SimpleComboBox from '@/components/SimpleComboBox.vue';
import CardWithDetails from '@/components/CardWithDetails.vue';
import ListItem from '@/components/ListItem.vue';
import TranslatedMessageDetail from '@/components/TranslatedMessageDetail.vue';

export default {
  components: {
    Button,
    Alert,
    Card,
    SimpleComboBox,
    CardWithDetails,
	ListItem,
	TranslatedMessageDetail
  },
  props: ["app", "translatedMessageName"],
  setup() {
    const lang = ref()
    return { lang }
  },
  data() {
		return {
			pageStart: 0
		};
	},
  methods: {
	  languageSelected(selectedLanguage){
		  this.lang = selectedLanguage.language_code
	  },
	  translatedMessageManaged() {
			this.$resources.candidates.reload()
			this.$router.push({ name: 'AppReview' })
		}
  },
  computed: {
		selectedCandidate() {
			return this.$resources.selectedCandidate.data;
		},
		candidates() {
			return this.$resources.candidates.data;
		},
		app_name() {
				return this.app.name;
		}
	},

	resources: {
		candidates() {
			this.lang = this.lang ?  this.lang : 'de'

			return {
				method: 'translator.api.get_translated_messsages_for_verification',
				params: {
					start: this.pageStart,
					lang: this.lang
				},
				auto: true,
				paged: true,
				keepData: true,
				default: [],
				onSuccess() {
					if (this.$resources.candidates.data[0]) {
						this.$router.push({ name: 'ReviewTranslatedMessage', params: {appName : this.app.name, translatedMessageName: this.$resources.candidates.data[0].name} })
					}
				},
			};
		},
		selectedCandidate() {
			this.lang = this.lang ?  this.lang : 'de'
			return {
				method: 'translator.api.get_translated_messsage_details',
				params: {
					translated_message_name: this.translatedMessageName,
				},
				validate() {
					if (!this.translatedMessageName) {
						return 'Select a candidate first';
					}
				},
				auto: true
			};
		}
	}
};
</script>
