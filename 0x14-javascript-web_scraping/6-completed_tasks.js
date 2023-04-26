const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to retrieve data: ${response.statusCode}`);
    return;
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  for (const task of tasks) {
    if (task.completed) {
      const userId = task.userId;
      if (!(userId in completedTasksByUser)) {
        completedTasksByUser[userId] = 1;
      } else {
        completedTasksByUser[userId]++;
      }
    }
  }

  console.log(completedTasksByUser);
});
