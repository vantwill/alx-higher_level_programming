#!/usr/bin/nod
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
  // console.log(data);
});

/*
const fs = require('fs');

try {
  const data = fs.readFileSync(process.argv[2], 'utf8');
  process.stdout.write(data);
  // console.log(data);
  // console.log(data.toString());
} catch (err);
  console.log(err);
  console.error(err);
}
*/
