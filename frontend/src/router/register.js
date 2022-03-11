export default [
	{
		path: '/register',
		name: 'Register',
		component: () =>
			import(/* webpackChunkName: "register" */ '../views/Register.vue'),
		props: true,
		meta: {
			isPublicPage: false,
			isLoginPage: false
		},
	},
];
