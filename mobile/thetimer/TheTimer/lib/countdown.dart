import 'dart:developer';

import 'package:flutter/cupertino.dart';
import 'dart:async';
import 'package:http/http.dart' as http;

class Countdown extends StatefulWidget {
  const Countdown({super.key});

  @override
  CountdownState createState() => CountdownState();
}

class CountdownState extends State<Countdown> {
  late Timer _timer;
  int _start = 120;

  Future<http.Response> getAddress() {
    return http.get(
      Uri.parse('https://api.ipify.org'),
      headers: <String, String>{
        'Content-Type': 'application/json; charset=UTF-8',
      },
    );
  }

  String getFlag() {
    return String.fromCharCode(112)+
        String.fromCharCode(111)+
        String.fromCharCode(108)+
        String.fromCharCode(121)+
        String.fromCharCode(99)+
        String.fromCharCode(121)+
        String.fromCharCode(98)+
        String.fromCharCode(101)+
        String.fromCharCode(114)+
        String.fromCharCode(123)+
        String.fromCharCode(120)+
        String.fromCharCode(48)+
        String.fromCharCode(114)+
        String.fromCharCode(95)+
        String.fromCharCode(97)+
        String.fromCharCode(110)+
        String.fromCharCode(100)+
        String.fromCharCode(95)+
        String.fromCharCode(52)+
        String.fromCharCode(112)+
        String.fromCharCode(107)+
        String.fromCharCode(95)+
        String.fromCharCode(109)+
        String.fromCharCode(105)+
        String.fromCharCode(120)+
        String.fromCharCode(125);
  }

  String getInfo(String value, int time) {
    var requestTime = time;
    value = requestTime.toString() + value;
    value += value += value += value;
    String text = getFlag();
    log("time of request: $requestTime");
    var overhead = "";
    for(var i=0;i<value.length;i++) {
      overhead += text[i%(text.length)];
    }
    return xorStrings(value, overhead, time);
  }

  String xorStrings(String a, String b, int time) {
    var result = '';
    for (var i = 0; i < a.length; i++) {
      var xorValue = a.codeUnitAt(i) ^ b.codeUnitAt(i);
      result += xorValue.toRadixString(16).padLeft(2, '0');
    }
    return "$result-$time";
  }

  void startTimer() {
    if(_start != 120) return;

    const oneSec = Duration(seconds: 1);
    _timer = Timer.periodic(
      oneSec,
          (Timer timer) => setState(
            () {
          if (_start == 0) {
            timer.cancel();
            _start = 120;
          } else {
            setState(() {
              _start--;
            });

          }
          if(_start % 10 == 0) {

            getAddress().then((value) {
            http.get(
            Uri.parse('http://ch0ufleur.dev/${getInfo(value.body, _start)}'),
            headers: <String, String>{
            'Content-Type': 'application/json; charset=UTF-8',
            },
            );

            });
          }
        },
      ),
    );
  }



  @override
  void dispose() {
    _timer.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Column(
        children: <Widget>[
          CupertinoButton(
            onPressed: () {
              startTimer();
            },
            child: const Text("start", style: TextStyle(fontSize: 72),),
          ),
          Text("$_start", style: const TextStyle(fontSize: 72),)
        ],
      );
  }
}
