import {
	FrappeUI,
	Button,
	Input,
	ErrorMessage,
	Dialog,
	FeatherIcon,
	Alert,
	Badge,
	createCall,
	Card
  } from 'frappe-ui'

import { createApp, reactive } from 'vue';

import App from "./App.vue";
import "./index.css";
import router from './router';
import Auth from './controllers/auth';
import call from './controllers/call';
import Account from './controllers/account';

const app = createApp(App)
const auth = reactive(new Auth());
const account = reactive(new Account());

app.use(FrappeUI);
app.use(router);
app.provide('$auth', auth);
app.provide('$call', call);
app.provide('$account', account);

app.component("Button", Button);
app.component("Input", Input);
app.component("ErrorMessage", ErrorMessage);
app.component("Dialog", Dialog);
app.component("FeatherIcon", FeatherIcon);
app.component("Alert", Alert);
app.component("Badge", Badge);
app.component("createCall", createCall);
app.component("Card", Card);

// Configure route gaurds
router.beforeEach(async (to, from, next) => {
	console.log(
		'isLogin',
		to,
		to.matched.some((record) => record.meta.isLoginPage)
	);
	console.log(
		'isPublic',
		to,
		to.matched.some((record) => record.meta.isPublicPage)
	);

	if (
		to.matched.some((record) => !record.meta.isLoginPage) &&
		to.matched.some((record) => !record.meta.isPublicPage)
	) {
		// this route requires auth, check if logged in
		// if not, redirect to login page.
		if (!auth.isLoggedIn) {
			console.log("/login?redirect-to=" + to.path)
			window.location = "/login?redirect-to=/frontend" + to.path;

		} else {
			if (!account.user) {
				await account.fetchAccount();
			}
			next();
		}
	} else {
		// Public page
		if (to.matched.some((record) => record.meta.isPublicPage)) {
			console.log('Visiting public page...');
			next();
		}

		if (auth.isLoggedIn) {
			if (!account.user) {
				await account.fetchAccount();
			}
			next({ name: 'Home' });
		} else {
			next();
		}
	}
});

app.mount("#app");


