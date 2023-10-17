// SPDX-License-Identifier: MIT
// 0x9195E7ADaFBf5642Dd1a1F20e4296624D7ac31cC deploy FC
// 0xcEab7Ca9c52AD5B4073f1911841d838a049e4F51 deploy SP
// 0x291f0E184dF75B6D68cE846f032Ee201ECD68591 scroll deploy

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