<template>
	<div>
		<Navbar />
    <div class="lg:container mx-auto">
		<router-view />
	</div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
	components: {
		Navbar,
	},
	inject: ['$auth'],
  data() {
		return {
			viewportWidth: 0
		};
	},
	provide: {
		viewportWidth: Math.max(
			document.documentElement.clientWidth || 0,
			window.innerWidth || 0
		)
	}
};
</script>