import { Web3Storage } from 'web3.storage';

// Constructor
const client = new Web3Storage({ token: "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkaWQ6ZXRocjoweDVhNzhjNEYyNDFFYTVlMjM0NTYxNDBBNmQ3RjM4MDJhQjg0OUREMWUiLCJpc3MiOiJ3ZWIzLXN0b3JhZ2UiLCJpYXQiOjE2OTc0NjI2NzEwNjIsIm5hbWUiOiJnYWJvdGVzdCJ9.Oc19qsVDqwYkcFvXcsmzImOfH_BINuhYnRrcG6r7fDY" })

const fileInput = document.querySelector('input[name="fileinn"]');

// Pack files into a CAR and send to web3.storage
const rootCid = await client.put(fileInput.files, {
  name: 'CleanCsv',
  maxRetries: 3,
});

console.log("rootCid");
