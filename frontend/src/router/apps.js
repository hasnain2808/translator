export default [
	{
		path: '/apps',
		name: 'Apps',
		component: () =>
			import(
				/* webpackChunkName: "apps" */ '../views/Apps.vue'
			)
	},
	{
		path: '/apps/:appName',
		name: 'App',
		component: () => import(/* webpackChunkName: "app" */ '../views/App.vue'),
		props: true,
		children: [
			{
				path: 'stats',
				component: () => import('../views/AppStats.vue')
			},
			{
				path: 'review',
				component: () => import('../views/AppReview.vue'),
				name: 'AppReview',
			},
			{
				path: 'review/:translatedMessageName',
				name: 'ReviewTranslatedMessage',
				component: () => import(/* webpackChunkName: "app" */ '../views/AppReview.vue'),
				props: true
			}
		]
	}
];


