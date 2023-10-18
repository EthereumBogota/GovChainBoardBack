// SPDX-License-Identifier: MIT
pragma solidity 0.5.16;

contract Utils {
    function getTimeStamop() public view returns (uint256) {

        return block.timestamp;

    }
}