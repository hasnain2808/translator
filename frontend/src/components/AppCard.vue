<template>
	<button
		class="flex self-stretch rounded-lg border bg-white p-3 shadow hover:border-gray-300 focus:outline-none"
	>
		<Avatar
			class="shrink-0"
			size="lg"
			shape="square"
			:imageURL="app.logo"
			:label="app.app_name"
		/>
		<div class="ml-3 w-full">
			<div class="flex items-center justify-between">
				<h2 class="text-left text-xl font-bold capitalize">
					{{ app.app_name }}
				</h2>
			</div>
			<p class="pt-1 text-left text-base text-gray-600">
				{{ app.description }}
			</p>
		</div>
	</button>
</template>

<script>
import Avatar from '@/components/Avatar.vue';

export default {
	props: ['app'],
	components: {
		Avatar,
	}
};
</script>
