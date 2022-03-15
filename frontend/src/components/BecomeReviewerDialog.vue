<template>
  <Dialog :options="{ title: 'Add Team' }" v-model="showDialog">
    <template #body-content>
      <div class = "mt-5">
        <label for="linkedin_url" class="block text-sm font-medium text-gray-700">Linkedin URL</label>
        <div class="mt-1">
          <input type="url" 
            name="linkedin_url" 
            v-model="linkedin_url"
            class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
            placeholder="Linkedin URL" />
        </div>
      </div>

      <div class = "mt-5">
        <label for="github_url" class="block text-sm font-medium text-gray-700">Github URL</label>
        <div class="mt-1">
          <input type="url" 
            name="github_url" 
            v-model="github_url"
            class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
            placeholder="Github URL" />
        </div>
      </div>

      <div class = "mt-5">
        <label for="portfolio_url" class="block text-sm font-medium text-gray-700">Portfolio URL</label>
        <div class="mt-1">
          <input type="url" 
            name="portfolio_url" 
            v-model="portfolio_url"
            class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
            placeholder="Portfolio URL" />
        </div>
      </div>

      <div class = "mt-5">
        <label for="reason" class="block text-sm font-medium text-gray-700">Reason</label>
        <div class="mt-1">
        <textarea
          name="reason" 
          v-model="reason"
          class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
          placeholder="Reason"
        />
        </div>
      </div>
    <div class = "mt-5">

    <SimpleComboBox ref="SimpleCombobox" @languageSelected="languageSelected"></SimpleComboBox>
</div>
      <ErrorMessage
        class="mt-2"
        :message="$resources.createReviewer.error"
      />
    </template>

    <template #actions>
      <Button
        appearance="primary"
        @click="$resources.createReviewer.submit()"
        :loading="$resources.createReviewer.loading"
      >
        Create Team
      </Button>
    </template>
  </Dialog>
</template>
<script>
import { Dialog } from 'frappe-ui'
import SimpleComboBox from '@/components/SimpleComboBox.vue';

export default {
  name: 'BecomeReviewerDialog',
  props: ['show'],
  emits: ['success', 'update:show'],
  data() {
    return {
      linkedin_url : '',
      github_url : '',
      portfolio_url : '',
      lang : '',
      reason: ''
    }
  },
  components: {
    Dialog,
    SimpleComboBox,

  },
  computed: {
    showDialog: {
      get() {
        return this.show
      },
      set(val) {
        this.$emit('update:show', val)
      },
    },
  },
  resources: {
    createReviewer() {
      return {
        method: 'translator.api.become_a_reviewer',
        params: {
          language: this.lang,
          linkedin_url: this.linkedin_url,
          github_url: this.github_url,
          portfolio_url: this.portfolio_url,
          reason: this.reason
        },
        validate() {
          if (!this.lang) {
            return 'Language is required'
          }
          if (!this.reason) {
            return 'Reason is required'
          }
        },
        onSuccess(reviewer) {
          this.$emit('success', reviewer)
        },
      }
    },
  },
  methods: {
	  languageSelected(selectedLanguage){
		  this.lang = selectedLanguage.language_code
	  },
  }
}
</script>
