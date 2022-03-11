

 <template>
  <Button @click="ping">Click me</Button>

  <div class="p-4 grid grid-cols-2 gap-4">
    <Card title="Heading" subtitle="Sub text">
      <div class="text-base">Card content</div>
    </Card>
    <Card title="Heading" subtitle="Sub text">
      <div class="text-base">Card content</div>
    </Card>
  </div>

  <p>{{ $resources.ping.data }}</p>
</template>


<script>
import { Button, Alert, Card } from "frappe-ui";
export default {
  components: {
    Button,
    Alert,
    Card,
  },
  resources: {
    ping() {
      return {
        method: "ping",
        onSuccess(d) {
          console.log(d);
        },
        auto: true,
        onError(d) {
          console.error(d);
        },
      };
    },
  },
  methods: {
    ping() {
      this.$resources.ping.fetch();
    },
  },
};
</script>
