<template>
	<div>
		<Navbar />
    <div class="lg:container mx-auto">
		<router-view />
	</div>
  </div>
  <Dialogs />

</template>

<script>
import Navbar from './components/Navbar.vue';
import { Dialogs } from '@/utils/dialogs'

export default {
	components: {
		Navbar,
		Dialogs
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