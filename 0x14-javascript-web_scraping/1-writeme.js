#!/usr/bin/node
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`The file ${process.argv[2]} has been saved!`);
});
