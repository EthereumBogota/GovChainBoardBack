import { Database } from "@tableland/sdk";
import { Wallet, getDefaultProvider } from "ethers";

// const privateKey ="4f6422a4cd35e64e4cdd3d4313fe789b3d27e709d9229784b8f0c2fd70e81518"; // Your private key
// const wallet = new Wallet(privateKey);
// To avoid connecting to the browser wallet (locally, port 8545).
// For example: "https://polygon-mumbai.g.alchemy.com/v2/YOUR_ALCHEMY_KEY"
const provider = getDefaultProvider("34.73.36.206:3000");
// const signer = wallet.connect(provider);

// // Create a database connection
// const db = new Database({ signer });
// const prefix = "my_table";


// // The table's `name` is in the format `{prefix}_{chainId}_{tableId}`
// const tableName = "create.txn?.name" ?? ""; // e.g., my_table_31337_2



// // Read the table
// const { results } = await db.prepare(`SELECT * FROM ${tableName};`).all();
// console.log(results);