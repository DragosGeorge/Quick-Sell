# Quick Sell

This code is intended to implement a system through which you can quickly sell items from both the regular inventory and the special inventory. Items eligible for sale will have a tooltip displaying text indicating the keys to be pressed and the text 'Sell item'. Considering that keyboard keys are displayed in the tooltip, you should have also implemented the system allowing to attach images in TextLine.

In case you don't have the additional systems, you can remove the corresponding parts of the code and still use it without them.

## How It Works

By pressing SHIFT + RIGHT CLICK on the items eligible for sale, an interface will appear showing you how much money you will receive and how many items you have selected. The selected items will have a special icon indicating that they have been selected.

## Demo

![Demo](example.gif)

## UPDATE

1.When the sales window appears, items that cannot be sold will be displayed in white.

2.While the window is open, items can no longer be moved to the inventory.

3.The selling prices of the items will appear in the tooltip when the window is open.

4.A log has been added to the interface, allowing you to see the names of the items you want to sell.

Files such as add-ons and button images have been added to the repository.
