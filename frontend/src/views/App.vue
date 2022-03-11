<template>
	<div class="mt-10">
		<div class="px-4 sm:px-8" v-if="app">
			<div class="pb-3">
				<div class="text-base text-gray-700">
					<router-link to="/apps" class="hover:text-gray-800">
						← Back to Apps
					</router-link>
				</div>
				<div
					class="flex flex-col space-y-3 md:flex-row md:items-baseline md:justify-between md:space-y-0"
				>
					<div class="mt-2 flex items-center">

					</div>
					<div v-if="bench.status == 'Active'">
						<Button icon-left="plus" :route="`/${app.name}/new`">
							New App
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

export default {
	name: 'App',
	props: ['AppName'],
	components: {
		Tabs
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
		}
	},
	activated() {
	},
	deactivated() {
	},
	methods: {

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
		}
	}
};
</script>
