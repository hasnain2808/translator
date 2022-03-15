import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import appsRoutes from './apps';
import reviewersRoutes from './reviewers';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
		meta: {
			isPublicPage: false,
		},
	},
	...appsRoutes,
	...reviewersRoutes,
	{
		path: '/your-applications',
		name: 'YourApplications',
		component: () => import(/* webpackChunkName: "app" */ '../views/YourApplications.vue'),
		meta: {
			isPublicPage: false,
		},
	},
	{
		path: '/your-applications/:reviewerName',
		name: 'YourApplicationsDetails',
		component: () => import(/* webpackChunkName: "app" */ '../views/YourApplications.vue'),
		props: true,
	}
];

const router = createRouter({
	history: createWebHistory('/translator/'),
	routes,
});

export default router;
