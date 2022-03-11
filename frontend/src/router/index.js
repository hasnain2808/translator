import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import registerRoutes from './register';
import appsRoutes from './apps';
// import purchaseRoutes from './purchase';

const routes = [
	{
		path: '/',
		name: 'Home',
		component: Home,
		meta: {
			isPublicPage: false,
		},
	},
	...registerRoutes,
	...appsRoutes,
];

const router = createRouter({
	base: '/frontend/',
	history: createWebHistory(),
	routes,
});

export default router;
