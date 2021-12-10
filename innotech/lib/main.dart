import 'package:flutter/material.dart';

//MAIN PAGE COLORS
Color mainPageBG = Color(0xff2D2F4E);

void main() {
  runApp(HomePage());
}

class HomePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("iNNOTECH"),
        ),
        backgroundColor: Color(0xff2D2F4E),
        body: Column(
          children: [
            Card(
              child: Column(
                children: <Widget>[
                  Image.asset('assets/logo.png'),
                  
                ],
              ),
            ),
            
          ],
        ),
      ),
    );
  }
}
