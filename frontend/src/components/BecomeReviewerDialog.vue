<template>
  <Dialog :options="{ title: 'Become a Reviewer' }" v-model="showDialog">
    <template #body-content>
          <Input type="text"
            name="linkedin_url"
            v-model="linkedin_url"
            label="Linkedin URL"
            class="mb-2"
            placeholder="Linkedin URL" />

          <Input type="text"
            name="github_url"
            v-model="github_url"
            label="Github URL"
            class="mb-2"
            placeholder="Github URL" />

          <Input type="text"
            name="portfolio_url"
            v-model="portfolio_url"
            class="mb-2"
            placeholder="Portfolio URL"
            label="Portfolio URL" />

          <Input type="textarea"
            name="reason"
            v-model="reason"
            class="mb-2"
            label="Reason"
            placeholder="Reason"
          />
    <SimpleComboBox ref="SimpleCombobox" @languageSelected="languageSelected"></SimpleComboBox>
      <ErrorMessage
        class="mt-2"
        :message="$resources.createReviewer.error.messages"
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
