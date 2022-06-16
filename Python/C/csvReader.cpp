#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

struct TorontoRealEstateRecord{
public:
    TorontoRealEstateRecord(
        int final_price,
        int list_price,
        int bedrooms,
        int bathrooms,
        int sqft,
        int parking,
        string type,
        string full_address
    ) {
        FinalPrice = final_price;
        ListPrice = list_price;
        Bedrooms = bedrooms;
        Bathrooms = bathrooms;
        Sqft = sqft;
        Parking = parking;
        Type = type;
        FullAddress = full_address;
    }

    void display() {
        cout << "   FinalPrice: " << final_price << endl;
        cout << "   ListPrice: " << list_price << endl;
        cout << "   Bedrooms: " << bedrooms << endl;
        cout << "   Bathrooms: " << bathrooms << endl;
        cout << "   Sqft: " << sqft << endl;
        cout << "   Parking: " << parking << endl;
        cout << "   Type: " << type << endl;
        cout << "   FullAddress: " << fullAddress << endl;
        cout << endl;
    }

    int final_price,
    int list_price,
    int bedrooms,
    int bathrooms,
    int sqft,
    int parking,
    string type,
    string full_address,

    };

void displayUnits(vector<TorontoRealEstateRecord>& TorontoRealEstateUnits) {

    for (auto TorontoRealEstateD : TorontoRealEstateUnits) {
        TorontoRealEstateD.display();
    }
}

        int main(){
        ifstream inputFile;
        inputFile.open("TorontoRealEstate.csv");
        string line = "";

        vector<TorontoRealEstateRecord> TorontoRealEstateUnits;
        while (getline(inputFile, line)){

            stringstream inputString(line);

            int final_price;
            int list_price;
            int bedrooms;
            int bathrooms;
            int sqft;
            int parking;
            string type;
            string full_address;

            final_price = atoi(tempString.c_str());
            list_price = atoi(tempString.c_str());
            bedrooms = atoi(tempString.c_str());
            bathrooms = atoi(tempString.c_str());
            sqft = atoi(tempString.c_str());
            parking = atoi(tempString.c_str());
            getline(inputString, type, ',');
            getline(inputString, full_address, ',');
            getline(inputString, tempString);

            TorontoRealEstateRecord TorontoRealEstateD(final_price, list_price, bedrooms, bathrooms, sqft, parking, type, full_address);
            TorontoRealEstateUnits.push_back(TorontoRealEstateD);
            line = "";
        }

        displayUnits(TorontoRealEstateUnits);
    }
