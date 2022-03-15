<template>
	<div class='mt-4'>
		<CardWithDetails
			title="Your Applications"
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
					:to="`/your-applications/${candidate.name}`"
				>
					<ListItem
						:title="` ${candidate.user}, applied for
							${candidate.language}
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
				<YourApplicationDetail
					:showDetails="selectedCandidate"
					:loading="$resources.selectedCandidate.loading"
					title="Your Details"
				/>
			</template>
		</CardWithDetails>
	</div>
</template>

<script>
import CardWithDetails from '@/components/CardWithDetails.vue';
import ListItem from '@/components/ListItem.vue';
import YourApplicationDetail from '@/components/YourApplicationDetail.vue';

export default {
	name: 'YourApplications',
	props: ['reviewerName'],
	components: {
		CardWithDetails,
		ListItem,
		YourApplicationDetail
	},
	data() {
		return {
			pageStart: 0
		};
	},
	resources: {
		candidates() {
			return {
				method: 'translator.api.get_your_applications',
				params: {
					start: this.pageStart
				},
				auto: true,
				paged: true,
				keepData: true,
				default: [],
				onSuccess() {
					if (this.$resources.candidates.data[0]) {
						this.$router.push({ name: 'YourApplicationsDetails', params: {reviewerName : this.$resources.candidates.data[0].name} });
					}
				},
			};
		},
		selectedCandidate() {
			return {
				method: 'translator.api.get_reviewer_application',
				params: {
					name: this.reviewerName
				},
				validate() {
					if (!this.reviewerName) {
						return 'Select a candidate first';
					}
				},
				auto: true
			};
		}
	},
	computed: {
		selectedCandidate() {
			return this.$resources.selectedCandidate.data;
		},
		candidates() {
			return this.$resources.candidates.data;
		}
	}
};
</script>
