class Auction:
    def __init__(self, item_name, starting_price):
        self.item_name = item_name
        self.starting_price = starting_price
        self.highest_bid = starting_price
        self.highest_bidder = None
        self.bids = []

    def place_bid(self, bidder_name, bid_amount):
        if bid_amount > self.highest_bid:
            self.highest_bid = bid_amount
            self.highest_bidder = bidder_name
            self.bids.append((bidder_name, bid_amount))
            print(f"New highest bid of ${bid_amount} by {bidder_name}")
        else:
            print(
                f"Bid of ${bid_amount} is lower than the current highest bid of ${self.highest_bid}"
            )

    def get_auction_status(self):
        if self.highest_bidder:
            return f"The highest bid is ${self.highest_bid} by {self.highest_bidder}."
        else:
            return f"No bids placed yet. Starting price is ${self.starting_price}."

    def end_auction(self):
        if self.highest_bidder:
            print(
                f"Auction ended. {self.item_name} sold to {self.highest_bidder} for ${self.highest_bid}."
            )
        else:
            print(f"Auction ended. No bids were placed for {self.item_name}.")


class AuctionSystem:
    def __init__(self):
        self.auctions = []

    def create_auction(self, item_name, starting_price):
        auction = Auction(item_name, starting_price)
        self.auctions.append(auction)
        print(f"Auction for {item_name} created with starting price ${starting_price}.")

    def list_auctions(self):
        if not self.auctions:
            print("No auctions available.")
            return
        for index, auction in enumerate(self.auctions):
            print(
                f"{index + 1}. Item: {auction.item_name}, Highest Bid: ${auction.highest_bid}"
            )

    def place_bid(self, auction_index, bidder_name, bid_amount):
        if 0 <= auction_index < len(self.auctions):
            self.auctions[auction_index].place_bid(bidder_name, bid_amount)
        else:
            print("Invalid auction index.")

    def end_auction(self, auction_index):
        if 0 <= auction_index < len(self.auctions):
            self.auctions[auction_index].end_auction()
            del self.auctions[auction_index]
        else:
            print("Invalid auction index.")


def main():
    system = AuctionSystem()

    while True:
        print("\nOnline Auction System")
        print("1. Create Auction")
        print("2. List Auctions")
        print("3. Place Bid")
        print("4. End Auction")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter the item name: ")
            starting_price = float(input("Enter the starting price: "))
            system.create_auction(item_name, starting_price)
        elif choice == "2":
            system.list_auctions()
        elif choice == "3":
            system.list_auctions()
            auction_index = int(input("Enter the auction number to place bid on: ")) - 1
            bidder_name = input("Enter your name: ")
            bid_amount = float(input("Enter your bid amount: "))
            system.place_bid(auction_index, bidder_name, bid_amount)
        elif choice == "4":
            system.list_auctions()
            auction_index = int(input("Enter the auction number to end: ")) - 1
            system.end_auction(auction_index)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
