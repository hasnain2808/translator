<template>
		<div class="container mx-auto">

	<div class="mt-8">

	<div>
		<Button
			v-if="$resources.apps.loading"
			:loading="true"
			loadingText="Loading..."
		></Button>
		<ErrorMessage
			v-else-if="!$resources.apps.data"
			:error="$resources.apps.error"
		/>
		<div v-else-if="$resources.apps.data.length < 1">
			<p class="text-lg text-gray-600">
				There are no apps available.
			</p>
		</div>
		<div v-else>
			<div class="grid grid-cols-1 gap-4 md:grid-cols-3">
				<AppCard
					@click.native="routeToAppPage(app.name)"
					v-for="app in $resources.apps.data"
					:key="app.name"
					:app="app"
				/>
			</div>
		</div>
	</div>
	</div>
	</div>
</template>

<script>
import AppCard from '@/components/AppCard.vue';

export default {
	name: 'Apps',
	components: {
		AppCard,
	},
	activated() {
		this.$resources.apps.fetch();
	},
	resources: {
		apps() {
			return {
				method: 'translator.api.get_apps',
				auto: true
			};
		}
	},
	methods: {
		routeToAppPage(appName) {
			this.$router.push(`/apps/${appName}`);
		}
	}
};
</script>
