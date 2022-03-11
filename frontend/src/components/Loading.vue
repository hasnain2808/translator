<template>
	<div class="flex items-center text-base text-gray-500">
		<LoadingIndicator /> {{ text }}
	</div>
</template>
<script>
import { LoadingIndicator } from 'frappe-ui'

export default {
	name: 'Loading',
	  components: {
    	LoadingIndicator,
  	},
	props: {
		text: {
			type: String,
			default: 'Loading...'
		}
	}
};
</script>
