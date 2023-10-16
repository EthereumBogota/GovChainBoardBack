// SPDX-License-Identifier: MIT
// 0x9195E7ADaFBf5642Dd1a1F20e4296624D7ac31cC deploy
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/governance/Governor.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorCountingSimple.sol";
import "@openzeppelin/contracts/governance/extensions/GovernorVotes.sol";

contract GovGCV is Governor, GovernorCountingSimple, GovernorVotes {
    constructor(IVotes _token) Governor("GovGCV") GovernorVotes(_token) {}

    function votingDelay() public pure override returns (uint256) {
        return 7200; // 1 day
    }

    function votingPeriod() public pure override returns (uint256) {
        return 21600; // 3 day
    }

    function quorum(uint256 blockNumber) public pure override returns (uint256) {
        return 2e18;
    }
}