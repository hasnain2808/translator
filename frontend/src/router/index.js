import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import registerRoutes from './register';
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
	...registerRoutes,
	...appsRoutes,
	...reviewersRoutes,
];

const router = createRouter({
	history: createWebHistory('/translator/'),
	routes,
});

export default router;
