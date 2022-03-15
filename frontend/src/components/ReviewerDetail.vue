<template>
	<CardDetails :showDetails="showDetails">

		<div class="px-6 py-5">
			<div class="flex items-baseline justify-between">
				<div class="flex items-baseline space-x-2">
					<h2 class="text-xl font-semibold">{{ title }}</h2>
				</div>
				<div class="flex items-center space-x-2">
					<Button class="bg-gray-100 hover:bg-gray-200 text-gray-900 focus:shadow-outline-gray" @click="reject">Reject</Button>
					<Button class="bg-gradient-blue hover:bg-gradient-none hover:bg-blue-500 text-white focus:shadow-outline-blue" @click="approve">Approve</Button>
				</div>
			</div>
		</div>

		<div class="divide-y flex-auto overflow-y-auto px-6 pb-5 " v-if="showDetails">
			<ListItem title="User" :description="showDetails.user || 'N/A'" />
			<ListItem title="Language" :description="showDetails.language || 'N/A'" />
			<ListItem title="LinkedIN" :description="showDetails.linkedin_url" v-if="showDetails.linkedin_url" />
			<ListItem title="GitHub" :description="showDetails.github_url" v-if="showDetails.github_url" />
			<ListItem title="Portfolio" :description="showDetails.portfolio_url" v-if="showDetails.portfolio_url" />
			<ListItem title="Language Certification" :description="showDetails.language_certification_url" v-if="showDetails.language_certification_url" />
			<ListItem title="Reason" :description="showDetails.reason" v-if="showDetails.reason" />
		</div>
		<div v-else>
			<Loading v-if="loading" />
			<span v-else class="text-base text-gray-600 px-6"> No item selected </span>
		</div>


	</CardDetails>
</template>
<script>
import CardDetails from '@/components/CardDetails.vue';
import Loading from '@/components/Loading.vue';
import ListItem from '@/components/ListItem.vue';

export default {
	name: 'ReviewerDetail',
	props: ['showDetails', 'title', 'subtitle', 'loading' ],
	components: {
		CardDetails,
		Loading,
		ListItem
	},
	inject: ['viewportWidth'],
	resources: {

		verify_reviewer() {
			return {
				method: 'translator.api.verify_reviewer',
				auto: false,
				validate() {
					if (!this.showDetails.name) {
						return 'Select a candidate first';
					}
				},
				onSuccess() {
					console.log("verified")
					this.$emit('reviewerManaged')
				}
			}
		},
		reject_reviewer() {
			return {
				method: 'translator.api.reject_reviewer',
				auto: false,
				validate() {
					if (!this.showDetails.name) {
						return 'Select a candidate first';
					}
				},
				onSuccess() {
					console.log("rejected")
					this.$emit('reviewerManaged')
				}
			}
		}
  },
  methods: {
		approve() {
			this.$resources.verify_reviewer.submit({
				reviewer_name: this.showDetails.name
			});
		},
		reject() {
			this.$resources.reject_reviewer.submit({
				reviewer_name: this.showDetails.name
			});
		}
  	},
};
</script>


