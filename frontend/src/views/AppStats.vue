

 <template>
  <SimpleComboBox ref="SimpleCombobox" @languageSelected="languageSelected"></SimpleComboBox>

  <NumberCard :stats="stats"></NumberCard>
<div class='pt-4 grid grid-cols-1 gap-5 sm:grid-cols-2'>
	<Card
		class="w-full "
		:style="{ height: viewportWidth > 768 ? 'calc(100vh - 22rem)' : null }"
		title= "Top Contributors"
		subtitle= 'A big thanks to our top linguists'

	>
		<TopContributorList :people="topContributors"></TopContributorList> 

	</Card>

	<Card
		class="w-full"
		:style="{ height: viewportWidth > 768 ? 'calc(100vh - 22rem)' : null }"
		title= "How to contribute translations"
	>
			<ol class="list-decimal">
				<li>Open <strong>Translations Tool</strong> from the awesome bar</li>
				<li>Select the language of your choice</li>
				<li>Click any source message from left sidebar for which you want to add translation.</li>
				<li>In the Translated Text field enter your suggested translation and click on <strong>Suggest</strong>.</li>
				<li>You can click on another source text from left sidebar and add another translation.</li>
				<li>Once you are done with all the translations you can click on <strong>Contribute Translations</strong> button.</li>
				<li>You can view the status of your contribution by clicking on the source text under Contributed Translations section.</li>
			</ol>
	</Card>

</div>


</template>


<script>

import NumberCard from '@/components/NumberCard.vue';
import SimpleComboBox from '@/components/SimpleComboBox.vue';
import TopContributorList from '@/components/TopContributorList.vue';
import {  ref } from 'vue'


export default {
  components: {
    NumberCard,
	SimpleComboBox,
	TopContributorList
  },
  props: ["app"],
  inject: ['viewportWidth'],
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

		},
		topContributors() {
			this.lang = this.lang ?  this.lang : 'de'
			return {
				method: 'translator.api.get_top_contributors',
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
		  this.$resources.topContributors.fetch();
		  console.log(this.$resources.stats)
		  console.log(this.$resources.topContributors)
	  }
  },
  computed: {
		stats() {
			if (this.$resources.stats.data && !this.$resources.stats.loading) {
				return this.$resources.stats.data;
			}
		},
		topContributors() {
			if (this.$resources.topContributors.data && !this.$resources.topContributors.loading) {
				return this.$resources.topContributors.data;
			}
		}
  }
};
</script>
