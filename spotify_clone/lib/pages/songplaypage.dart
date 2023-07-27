import 'package:flutter/material.dart';

class MySongPlayerPage extends StatefulWidget {
  final int songid;
  const MySongPlayerPage({super.key, required this.songid});

  @override
  State<MySongPlayerPage> createState() => _MySongPlayerPageState();
}

class _MySongPlayerPageState extends State<MySongPlayerPage> {
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
      appBar: AppBar(
        title:const Text('song name'),
        centerTitle: true,
      ),
      body:const Center(
        child: Column(
          children: [

          ],
        ),
      ),
    );
  }
}