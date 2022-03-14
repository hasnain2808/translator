<template>
	<div class="mt-10">
		<div class="px-4 sm:px-8" v-if="app">
			<div >
				<div class="text-base text-gray-700">
					<router-link to="/apps" class="hover:text-gray-800">
						← Back to Apps
					</router-link>
				</div>
				<div
					class="flex flex-col space-y-3 md:flex-row  md:justify-between md:space-y-0 py-4"
				>
					<div class="flex" >
						<div>
							<Avatar
								class="shrink-0"
								size="lg"
								shape="square"
								:imageURL="app.logo"
								:label="app.app_name"
							/>
						</div>
						<div class="flex items-center mx-2">
							<h1 class="text-2xl mb-0  font-bold">{{ app.app_name }}</h1>
						</div>
					</div>
					<div class="flex items-center">
						<Button icon-left="plus">
							Become a Reviewer
						</Button>
					</div>
				</div>
			</div>
		</div>
		<div class="px-4 sm:px-8" v-if="app">
			<Tabs class="pb-32" :tabs="tabs">
				<router-view v-bind="{ app }"></router-view>
			</Tabs>
		</div>
	</div>
</template>

<script>
import Tabs from '@/components/Tabs.vue';
import Avatar from '@/components/Avatar.vue';

export default {
	name: 'App',
	props: ['appName'],
	components: {
		Tabs,
		Avatar
	},
	resources: {
		app() {

			return {
				method: 'translator.api.get_app',
				params: {
					name: this.appName
				},
				auto: true
			};
		},

	},
	computed: {
		tabs() {
			let tabRoute = subRoute => `/apps/${this.appName}/${subRoute}`;
			let tabs = [
				{ label: 'Stats', route: 'stats' },
				{ label: 'Review', route: 'review' }
			];
			if (this.app) {
				return tabs.map(tab => {
					return {
						...tab,
						route: tabRoute(tab.route)
					};
				});
			}
			return [];
		},
		app() {
			if (this.$resources.app.data && !this.$resources.app.loading) {
				return this.$resources.app.data;
			}
		}
	},
	activated() {
		let tabRoute = subRoute => `/apps/${this.appName}/${subRoute}`;
		console.log("activated");
		console.log(this.tabs);
		if (!this.$route.path.split('/')[3]) {
			this.$router.replace(tabRoute(this.tabs[0].route));
		}
	},
};
</script>
