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
	}
];
