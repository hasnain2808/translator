<template>
	<CardDetails :showDetails="showDetails">

		<div class="px-6 py-5" v-if="showDetails">
			<div class="flex items-baseline justify-between">
				<div class="flex items-baseline space-x-2">
					 <h2 class="text-xl font-semibold">Contributed Translation</h2>
				</div>
				<div class="flex items-center space-x-2">
					<Button class="bg-gray-100 hover:bg-gray-200 text-gray-900 focus:shadow-outline-gray" @click="reject">Reject</Button>
					<Button class="bg-gradient-blue hover:bg-gradient-none hover:bg-blue-500 text-white focus:shadow-outline-blue" @click="approve">Approve</Button>
				</div>
			</div>
		</div>

		<div class="divide-y flex-auto overflow-y-auto px-6 pb-5 " v-if="showDetails">
			<ListItem title="Source Message" :description="showDetails.source.message || 'N/A'" />
			<ListItem title="Translated Message" :description="showDetails.translated.translated || 'N/A'" />
			<ListItem title="Context" :description="showDetails.source.context" v-if="showDetails.source.context" />
			<div v-for="position in showDetails.source.positions" v-if="showDetails.source.positions">
				<ListItem title="App Version" :description="position.app_version"  v-if="position.app_version" />
				<ListItem title="Module" :description="position.module"  v-if="position.app_version" />
				<ListItem title="Type" :description="position.type"  v-if="position.type" />
				<ListItem title="Name" :description="position.document_name"  v-if="position.app_version" />
				<ListItem title="Postion" :description="position.position"  v-if="position.position" />
				<ListItem title="Line Number" :description="position.line_no"  v-if="position.line_no" />
			</div>
		</div>
		<div v-else class="mt-6">
			<Loading v-if="loading" />
			<span v-else class="text-base text-gray-600 px-6 "> No item selected </span>
		</div>


	</CardDetails>
</template>
<script>
import CardDetails from '@/components/CardDetails.vue';
import Loading from '@/components/Loading.vue';
import ListItem from '@/components/ListItem.vue';

export default {
	name: 'TranslatedMessageDetail',
	props: ['showDetails', 'title', 'subtitle', 'loading' ],
	components: {
		CardDetails,
		Loading,
		ListItem
	},
	inject: ['viewportWidth', 'appName'],
	resources: {
		verify_translated_messsage() {
			return {
				method: 'translator.api.verify_translated_messsage',
				auto: false,
				validate() {
					if (!this.showDetails.translated.name) {
						return 'Select a candidate first';
					}
				},
				onSuccess() {
					console.log("verified")
					this.$emit('translatedMessageManaged')
				},
			}
		},
		reject_translated_messsage() {
			return {
				method: 'translator.api.reject_translated_messsage',
				auto: false,
				validate() {
					if (!this.showDetails.translated.name) {
						return 'Select a candidate first';
					}
				},
				onSuccess() {
					console.log("rejected")
					this.$emit('translatedMessageManaged')
				},
			}
		}
  	},
	methods: {
		approve() {
			this.$resources.verify_translated_messsage.submit({
				translated_message_name: this.showDetails.translated.name
			});
		},
		reject() {
			this.$resources.reject_translated_messsage.submit({
				translated_message_name: this.showDetails.translated.name
			});
		}
	},
	computed: {
		processed_postions() {
			if (this.showDetails.source.positions) {
				for (const postion in this.showDetails.source.positions) {
					if (position.app == this.appName) {
						continue
					}
				}
			}
		}
	}
};
</script>


