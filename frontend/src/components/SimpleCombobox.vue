<!--
  This example requires Tailwind CSS v2.0+ 
  
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
  <Combobox as="div" v-model="selectedLanguage" >
    <ComboboxLabel class="mb-2 block text-sm leading-4 text-gray-700">Language</ComboboxLabel>
    <div class="relative mt-1">
      <ComboboxInput class="w-full form-input block rounded-none" @change="query = $event.target.value" :display-value="(language) => language.language_name" />
      <ComboboxButton class="absolute inset-y-0 right-0 flex items-center rounded-r-md px-2 focus:outline-none">
        <SelectorIcon class="h-5 w-5 text-gray-400" aria-hidden="true" />
      </ComboboxButton>

      <ComboboxOptions v-if="filteredLanguage && filteredLanguage.length > 0" class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm">
        <ComboboxOption v-for="language in filteredLanguage" :key="language.name" :value="language" as="template" v-slot="{ active, selected }">
          <li :class="['relative cursor-default select-none py-2 pl-3 pr-9', active ? 'bg-indigo-600 text-white' : 'text-gray-900']">
            <span :class="['block truncate', selected && 'font-semibold']">
              {{ language.language_name }}
            </span>

            <span v-if="selected" :class="['absolute inset-y-0 right-0 flex items-center pr-4', active ? 'text-white' : 'text-indigo-600']">
              <CheckIcon class="h-5 w-5" aria-hidden="true" />
            </span>
          </li>
        </ComboboxOption>
      </ComboboxOptions>
    </div>
  </Combobox>
</template>

<script>
import { computed, ref } from 'vue'
import { CheckIcon, SelectorIcon } from '@heroicons/vue/solid'
import {
  Combobox,
  ComboboxButton,
  ComboboxInput,
  ComboboxLabel,
  ComboboxOption,
  ComboboxOptions,
} from '@headlessui/vue'

const languages = [
 {
  "language_code": "af",
  "language_name": "Afrikaans"
 },
 {
  "language_code": "am",
  "language_name": "\u12a0\u121b\u122d\u129b"
 },
 {
  "language_code": "ar",
  "language_name": "\u0627\u0644\u0639\u0631\u0628\u064a\u0629"
 },
 {
  "language_code": "bg",
  "language_name": "B\u01celgarski"
 },
 {
  "language_code": "bn",
  "language_name": "\u09ac\u09be\u0999\u09be\u09b2\u09bf"
 },
 {
  "language_code": "bo",
  "language_name": "\u0f63\u0fb7\u0f0b\u0f66\u0f60\u0f72\u0f0b\u0f66\u0f90\u0f51\u0f0b"
 },
 {
  "language_code": "bs",
  "language_name": "Bosanski"
 },
 {
  "language_code": "ca",
  "language_name": "Catal\u00e0"
 },
 {
  "language_code": "cs",
  "language_name": "\u010desky"
 },
 {
  "language_code": "da",
  "language_name": "Dansk"
 },
 {
  "language_code": "da-DK",
  "language_name": "Dansk (Danmark)"
 },
 {
  "language_code": "de",
  "language_name": "Deutsch"
 },
 {
  "language_code": "el",
  "language_name": "\u03b5\u03bb\u03bb\u03b7\u03bd\u03b9\u03ba\u03ac"
 },
 {
  "language_code": "en",
  "language_name": "English"
 },
 {
  "language_code": "en-GB",
  "language_name": "English (United Kingdom)"
 },
 {
  "language_code": "en-US",
  "language_name": "English (United States)"
 },
 {
  "language_code": "es",
  "language_name": "Espa\u00f1ol"
 },
 {
  "language_code": "es-AR",
  "language_name": "Espa\u00f1ol (Argentina)"
 },
 {
  "language_code": "es-BO",
  "language_name": "Espa\u00f1ol (Bolivia)"
 },
 {
  "language_code": "es-CL",
  "language_name": "Espa\u00f1ol (Chile)"
 },
 {
  "language_code": "es-CO",
  "language_name": "Espa\u00f1ol (Colombia)"
 },
 {
  "language_code": "es-DO",
  "language_name": "Espa\u00f1ol (Rep\u00fablica Dominicana)"
 },
 {
  "language_code": "es-EC",
  "language_name": "Espa\u00f1ol (Ecuador)"
 },
 {
  "language_code": "es-GT",
  "language_name": "Espa\u00f1ol (Guatemala)"
 },
 {
  "language_code": "es-MX",
  "language_name": "Espa\u00f1ol (M\u00e9xico)"
 },
 {
  "language_code": "es-NI",
  "language_name": "Espa\u00f1ol (Nicaragua)"
 },
 {
  "language_code": "es-PE",
  "language_name": "Espa\u00f1ol (Per\u00fa)"
 },
 {
  "language_code": "et",
  "language_name": "Eesti"
 },
 {
  "language_code": "fa",
  "language_name": "\u067e\u0627\u0631\u0633\u06cc"
 },
 {
  "language_code": "fi",
  "language_name": "Suomi"
 },
 {
  "language_code": "fil",
  "language_name": "Filipino"
 },
 {
  "language_code": "fr",
  "language_name": "Fran\u00e7ais"
 },
 {
  "language_code": "fr-CA",
  "language_name": "Fran\u00e7ais Canadien"
 },
 {
  "language_code": "gu",
  "language_name": "\u0a97\u0ac1\u0a9c\u0ab0\u0abe\u0aa4\u0ac0"
 },
 {
  "language_code": "he",
  "language_name": "\u05e2\u05d1\u05e8\u05d9\u05ea"
 },
 {
  "language_code": "hi",
  "language_name": "\u0939\u093f\u0902\u0926\u0940"
 },
 {
  "language_code": "hr",
  "language_name": "Hrvatski"
 },
 {
  "language_code": "hu",
  "language_name": "Magyar"
 },
 {
  "language_code": "id",
  "language_name": "Indonesia"
 },
 {
  "language_code": "is",
  "language_name": "\u00edslenska"
 },
 {
  "language_code": "it",
  "language_name": "Italiano"
 },
 {
  "language_code": "ja",
  "language_name": "\u65e5\u672c\u8a9e"
 },
 {
  "language_code": "km",
  "language_name": "\u1797\u17b6\u179f\u17b6\u1781\u17d2\u1798\u17c2\u179a"
 },
 {
  "language_code": "kn",
  "language_name": "\u0c95\u0ca8\u0ccd\u0ca8\u0ca1"
 },
 {
  "language_code": "ko",
  "language_name": "\ud55c\uad6d\uc758"
 },
 {
  "language_code": "ku",
  "language_name": "\u06a9\u0648\u0631\u062f\u06cc"
 },
 {
  "language_code": "lo",
  "language_name": "\u0ea5\u0eb2\u0ea7"
 },
 {
  "language_code": "lt",
  "language_name": "Lietuvi\u0173 kalba"
 },
 {
  "language_code": "lv",
  "language_name": "Latvie\u0161u valoda"
 },
 {
  "language_code": "mk",
  "language_name": "\u043c\u0430\u043a\u0435\u0434\u043e\u043d\u0441\u043a\u0438"
 },
 {
  "language_code": "ml",
  "language_name": "\u0d2e\u0d32\u0d2f\u0d3e\u0d33\u0d02"
 },
 {
  "language_code": "mr",
  "language_name": "\u092e\u0930\u093e\u0920\u0940"
 },
 {
  "language_code": "ms",
  "language_name": "Melayu"
 },
 {
  "language_code": "my",
  "language_name": "\u1019\u103c\u1014\u103a\u1019\u102c"
 },
 {
  "language_code": "nl",
  "language_name": "Nederlands"
 },
 {
  "language_code": "no",
  "language_name": "Norsk"
 },
 {
  "language_code": "pl",
  "language_name": "Polski"
 },
 {
  "language_code": "ps",
  "language_name": "\u067e\u069a\u062a\u0648"
 },
 {
  "language_code": "pt",
  "language_name": "Portugu\u00eas"
 },
 {
  "language_code": "pt-BR",
  "language_name": "Portugu\u00eas Brasileiro"
 },
 {
  "language_code": "ro",
  "language_name": "Rom\u00e2n"
 },
 {
  "language_code": "ru",
  "language_name": "\u0440\u0443\u0441\u0441\u043a\u0438\u0439"
 },
 {
  "language_code": "rw",
  "language_name": "Kinyarwanda"
 },
 {
  "language_code": "si",
  "language_name": "\u0dc3\u0dd2\u0d82\u0dc4\u0dbd"
 },
 {
  "language_code": "sk",
  "language_name": "Sloven\u010dina (Slovak)"
 },
 {
  "language_code": "sl",
  "language_name": "Sloven\u0161\u010dina (Slovene)"
 },
 {
  "language_code": "sq",
  "language_name": "Shqiptar"
 },
 {
  "language_code": "sr",
  "language_name": "\u0441\u0440\u043f\u0441\u043a\u0438"
 },
 {
  "language_code": "sr-BA",
  "language_name": "Srpski"
 },
 {
  "language_code": "sv",
  "language_name": "Svenska"
 },
 {
  "language_code": "sw",
  "language_name": "Swahili"
 },
 {
  "language_code": "ta",
  "language_name": "\u0ba4\u0bae\u0bbf\u0bb4\u0bcd"
 },
 {
  "language_code": "te",
  "language_name": "\u0c24\u0c46\u0c32\u0c41\u0c17\u0c41"
 },
 {
  "language_code": "th",
  "language_name": "\u0e44\u0e17\u0e22"
 },
 {
  "language_code": "tr",
  "language_name": "Türkçe"
 },
 {
  "language_code": "uk",
  "language_name": "\u0443\u043a\u0440\u0430\u0457\u043d\u0441\u044c\u043a\u0430"
 },
 {
  "language_code": "ur",
  "language_name": "\u0627\u0631\u062f\u0648"
 },
 {
  "language_code": "uz",
  "language_name": "\u040e\u0437\u0431\u0435\u043a"
 },
 {
  "language_code": "vi",
  "language_name": "Vi\u1ec7t"
 },
 {
  "language_code": "zh",
  "language_name": "\u7b80\u4f53\u4e2d\u6587"
 },
 {
  "language_code": "zh-TW",
  "language_name": "\u7e41\u9ad4\u4e2d\u6587"
 }
]


export default {
  components: {
    CheckIcon,
    Combobox,
    ComboboxButton,
    ComboboxInput,
    ComboboxLabel,
    ComboboxOption,
    ComboboxOptions,
    SelectorIcon,
  },
  setup() {
    const query = ref('')
    const selectedLanguage = ref()
    const filteredLanguage = computed(() =>
      query.value === ''
        ? languages
        : languages.filter((language) => {
            return language.language_name.toLowerCase().includes(query.value.toLowerCase())
          })
    )
    return {
      query,
      selectedLanguage,
      filteredLanguage,
    }
  },
  mounted() {
    this.selectedLanguage = {
      "language_code": "es",
      "language_name": "Espa\u00f1ol"
    }
  },
  watch: {
    selectedLanguage: function() {

        this.$emit('languageSelected', this.selectedLanguage)
      }
  }
}
</script>