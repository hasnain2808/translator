export default [
	{
		path: '/reviewers',
		name: 'Reviewers',
		component: () =>
			import(
				/* webpackChunkName: "Reviewer" */ '../views/ReviewerApplications.vue'
			),
	},
	{
		path: '/reviewers/:reviewerName',
		name: 'ReviewersDetails',
		component: () => import(/* webpackChunkName: "app" */ '../views/ReviewerApplications.vue'),
		props: true,
	}

];
