import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ResourcesScreen extends StatefulWidget {
  @override
  _ResourcesScreenState createState() => _ResourcesScreenState();
}

class _ResourcesScreenState extends State<ResourcesScreen> {
  late Future<List<dynamic>> resources;

  @override
  void initState() {
    super.initState();
    resources = ApiService.fetchResources();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Resources')),
      body: FutureBuilder<List<dynamic>>(
        future: resources,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return Center(child: CircularProgressIndicator());
          } else if (snapshot.hasError) {
            return Center(child: Text('Error: ${snapshot.error}'));
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.length,
              itemBuilder: (context, index) {
                final resource = snapshot.data![index];
                return ListTile(
                  title: Text(resource['title']),
                  subtitle: Text(resource['description']),
                  onTap: () {
                    // Handle resource click (e.g., open link)
                  },
                );
              },
            );
          }
        },
      ),
    );
  }
}
