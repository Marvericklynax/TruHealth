class Resource {
  final String title;
  final String description;
  final String url;

  Resource({required this.title, required this.description, required this.url});

  factory Resource.fromJson(Map<String, dynamic> json) {
    return Resource(
      title: json['title'],
      description: json['description'],
      url: json['url'],
    );
  }
}
