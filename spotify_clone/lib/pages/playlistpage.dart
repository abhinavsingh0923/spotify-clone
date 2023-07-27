import 'package:flutter/material.dart';


class MyPlaylist extends StatefulWidget {
  const MyPlaylist({super.key});

  @override
  State<MyPlaylist> createState() => _MyPlaylistState();
}

class _MyPlaylistState extends State<MyPlaylist> {
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title:const Text("My playlist"),
        centerTitle: true,
      ),
      body:const Column(
        children: [

        ],
      ),
    );
  }
}