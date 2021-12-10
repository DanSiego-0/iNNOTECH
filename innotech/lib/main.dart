import 'package:flutter/material.dart';
import 'package:innotech/mysql.dart';
import 'package:mysql1/mysql1.dart';

void main() {
  runApp(UserPage());
}

class UserPage extends StatefulWidget {
var db = new Mysql();
var points = 0;

void _getPoints() {
}
  @override 
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Color(0xff2D2F4E),
       body: Column(
         children: <Widget>[

            Center(child: Container(
              padding: EdgeInsets.fromLTRB(0, 100.0, 0, 10.0),
              child: Text("Your Balance",
              style: TextStyle(fontSize: 20,fontWeight: FontWeight.bold,color: Colors.white),)
            )),
            Center(child: Container(
              padding: EdgeInsets.fromLTRB(0, 30, 0, 20),
              child: Text("1559",
              style: TextStyle(fontSize: 50,fontWeight: FontWeight.bold,color: Colors.white),)
            )),
            Center(child: Row(
              children: <Widget>[
                Expanded(
                  child: RaisedButton(
                    color: Colors.transparent,
                    onPressed: () {},
                    child: Text("Voucher Wallet",
                    style: TextStyle(fontSize: 15,fontWeight: FontWeight.bold,color:Colors.white))
                  ),
                ),
                Expanded(
                  child: RaisedButton(
                    color: Colors.transparent,
                    child: Text("Redeem Vouchers",
                    style: TextStyle(fontSize: 15,fontWeight: FontWeight.bold,color: Colors.white)),
                    onPressed: () {},
                  )
                )
              
              ],
            ))
         ],
       )
      ),
    );
  }
}


