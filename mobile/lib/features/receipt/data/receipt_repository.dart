import 'dart:io';
import 'package:dio/dio.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:mobile/features/auth/data/auth_repository.dart';

final receiptRepositoryProvider = Provider((ref) => ReceiptRepository(ref));

class ReceiptRepository {
  final Ref _ref;
  final Dio _dio = Dio(BaseOptions(baseUrl: 'http://10.0.2.2:8001'));

  ReceiptRepository(this._ref);

  Future<void> uploadReceipt(File image) async {
    final token = await _ref.read(authRepositoryProvider).getToken();
    if (token == null) throw Exception('Not authenticated');

    String fileName = image.path.split('/').last;
    FormData formData = FormData.fromMap({
      "file": await MultipartFile.fromFile(image.path, filename: fileName),
    });

    try {
      await _dio.post(
        '/receipts/',
        data: formData,
        options: Options(
          headers: {
            "Authorization": "Bearer $token",
            "Content-Type": "multipart/form-data",
          },
        ),
      );
    } catch (e) {
      throw Exception('Failed to upload receipt: $e');
    }
  }

  Future<List<dynamic>> getReceipts() async {
    final token = await _ref.read(authRepositoryProvider).getToken();
    if (token == null) return [];

    try {
      final response = await _dio.get(
        '/receipts/',
        options: Options(headers: {"Authorization": "Bearer $token"}),
      );
      return response.data;
    } catch (e) {
      return [];
    }
  }
}
