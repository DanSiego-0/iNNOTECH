import 'package:mysql1/mysql1.dart';


class Mysql {
  static String host = '34.124.202.8',user= 'root',password = 'password', db = 'innotech';
  static int port=3306;

  Mysql();

  Future<MySqlConnection> getConnection() async {
    var setting = new ConnectionSettings(
      host:host,
      port: port,
      user:user,
      password: password,
      db: db
    );
    return await MySqlConnection.connect(setting);
  }

}

