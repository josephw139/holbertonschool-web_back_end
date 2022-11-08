import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';
const expect = require('chai').expect;


const queue = kue.createQueue();

describe('tests createPushNotificationsJobs', () => {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it('test kue - success', function() {
    createPushNotificationsJobs([
      {
        phoneNumber: '0123456789',
        message: 'This is the code 1234 to verify your account',
      },
      {
        phoneNumber: '0123456789',
        message: 'This is the code 1234 to verify your account',
      },
    ], queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
  });

  it('tests kue - error', function() {
    expect(() => createPushNotificationsJobs('NotAnArray', queue)).to.throw(Error, 'Jobs is not an array');
  });
})
