

 <template>
  <SimpleComboBox ref="SimpleCombobox" @languageSelected="languageSelected"></SimpleComboBox>

</template>

<script>
import { Button, Alert, Card } from "frappe-ui";
import {  ref } from 'vue'
import SimpleComboBox from '@/components/SimpleComboBox.vue';


export default {
  components: {
    Button,
    Alert,
    Card,
    SimpleComboBox
  },
  props: ["app"],
  setup() {
    const lang = ref()
    return { lang }
  },
  methods: {
	  languageSelected(selectedLanguage){
		  this.lang = selectedLanguage.language_code
	  }
  }
};
</script>
