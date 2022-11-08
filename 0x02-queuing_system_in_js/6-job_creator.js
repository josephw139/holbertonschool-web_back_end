const kue = require('kue');
const queue = kue.createQueue();

const job = {
  phoneNumber: "string",
  message: "string",
}

const push_notif = queue.create('push_notification_code', job).save(
  function (err) {
    if (err) {
      console.log('Notification job failed');
    } else {
      console.log(`Notification job created: ${push_notif.id}`);
    }
  }
).on('complete', () => {
  console.log('Notification job completed');
});
