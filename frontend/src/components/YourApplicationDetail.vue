<template>
	<CardDetails :showDetails="showDetails">

		<div class="px-6 py-5">
			<div class="flex items-baseline justify-between">
				<div class="flex  space-x-2">
					<h2 class="text-xl font-semibold">Details</h2>
					<Badge v-if="showDetails && showDetails.status " :status="showDetails.status">{{showDetails.status}}</Badge>
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
	name: 'YourApplicationDetail',
	props: ['showDetails', 'title', 'subtitle', 'loading' ],
	components: {
		CardDetails,
		Loading,
		ListItem
	},
	inject: ['viewportWidth']

};
</script>


