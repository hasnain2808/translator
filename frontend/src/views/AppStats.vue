

 <template>
  <SimpleComboBox ref="SimpleCombobox" @languageSelected="languageSelected"></SimpleComboBox>

  <NumberCard :stats="stats"></NumberCard>

<div v-if="this.$refs.SimpleCombobox">
	{{ this.$refs.SimpleCombobox.selectedLanguage}}
	</div>
</template>


<script>

import NumberCard from '@/components/NumberCard.vue';
import SimpleComboBox from '@/components/SimpleComboBox.vue';
import {  ref } from 'vue'


export default {
  components: {
    NumberCard,
	SimpleComboBox
  },
  props: ["app"],
  setup() {
	const lang = ref()
	return { lang }
  },
  resources: {
		stats() {
			this.lang = this.lang ?  this.lang : 'de'
			return {
				method: 'translator.api.get_application_stats',
				params: {
					app_name: this.app.name,
					lang: this.lang
				},
				auto: true
			};

		}
  },
  methods: {
	  languageSelected(selectedLanguage){
		  this.lang = selectedLanguage.language_code
		  this.$resources.stats.fetch();
		  console.log(this.$resources.stats)
	  }
  },
  computed: {
		stats() {
			if (this.$resources.stats.data && !this.$resources.stats.loading) {
				return this.$resources.stats.data;
			}
		}
  }
};
</script>
