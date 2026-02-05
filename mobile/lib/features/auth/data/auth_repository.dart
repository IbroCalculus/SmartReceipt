import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

// Provider for AuthRepository
final authRepositoryProvider = Provider((ref) => AuthRepository());

class AuthRepository {
  final Dio _dio = Dio(
    BaseOptions(baseUrl: 'http://10.0.2.2:8001'),
  ); // Emulator localhost
  final _storage = const FlutterSecureStorage();

  Future<String?> login(String email, String password) async {
    try {
      final response = await _dio.post(
        '/token',
        data: {'username': email, 'password': password},
        options: Options(contentType: Headers.formUrlEncodedContentType),
      );

      final token = response.data['access_token'];
      await _storage.write(key: 'jwt_token', value: token);
      return token;
    } catch (e) {
      throw Exception('Login Failed: $e');
    }
  }

  Future<void> logout() async {
    await _storage.delete(key: 'jwt_token');
  }

  Future<String?> getToken() async {
    return await _storage.read(key: 'jwt_token');
  }
}
