import "@nomicfoundation/hardhat-toolbox"
import "hardhat-deploy"
import "hardhat-deploy-ethers"
import "./tasks/deploy" // Your deploy task.
import "./tasks/0_join-dao"
import "./tasks/1_create-deal"
import "./tasks/2_approve-deal"
import "./tasks/3_activate-deal"
import "./tasks/4_collect-reward"

/** @type import('hardhat/config').HardhatUserConfig */
export const solidity = "0.8.17"
export const defaultNetwork = "hyperspace"
export const networks = {
    hyperspace: {
        chainId: 3141,
        url: " https://wss.hyperspace.node.glif.io/apigw/lotus/rpc/v1",
        accounts: [PRIVATE_KEY],
    },
}
export const paths = {
    sources: "./contracts",
    tests: "./test",
    cache: "./cache",
    artifacts: "./artifacts",
}