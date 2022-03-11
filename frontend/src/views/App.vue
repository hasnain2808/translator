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
		
		</div>
	</div>
	</div>
	</div>
</template>

<script>

import ErrorMessage from '@/components/ErrorMessage.vue';

export default {
	name: 'App',
	props: ['appName'],
	components: {
		ErrorMessage
	},
	activated() {

		this.$resources.apps.fetch();
	},
	resources: {
		apps() {
			console.log("hello")
			console.log(this.appName)
			return {
				method: 'translator.api.get_apps',
				auto: true
			};
		}
	},
	methods: {
	}
};
</script>
