import java.sql.*;

public class UserDao {

    // H2 데이터베이스 연결 정보
    private static final String DB_URL = "jdbc:h2:mem:testdb";
    private static final String DB_USER = "sa";
    private static final String DB_PASSWORD = "";

    // DB 연결 메서드
    private Connection getConnection() throws SQLException, ClassNotFoundException {
        Class.forName("org.h2.Driver");
        return DriverManager.getConnection(DB_URL, DB_USER, DB_PASSWORD);
    }

    // 테이블 생성 (애플리케이션 시작 시 호출)
    public void initializeDatabase() throws SQLException, ClassNotFoundException {
        String createTableSQL = """
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR(255) PRIMARY KEY,
                name VARCHAR(255),
                password VARCHAR(255)
            );
        """;

        try (Connection c = getConnection();
             Statement stmt = c.createStatement()) {
            stmt.execute(createTableSQL);
        }
    }

    // 사용자 추가
    public void add(User user) throws SQLException, ClassNotFoundException {
        String sql = "INSERT INTO users(id, name, password) VALUES(?,?,?)";

        try (Connection c = getConnection();
             PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, user.getId());
            ps.setString(2, user.getName());
            ps.setString(3, user.getPassword());
            ps.executeUpdate();
        }
    }

    // 사용자 조회
    public User get(String id) throws SQLException, ClassNotFoundException {
        String sql = "SELECT * FROM users WHERE id = ?";

        try (Connection c = getConnection();
             PreparedStatement ps = c.prepareStatement(sql)) {
            ps.setString(1, id);

            try (ResultSet rs = ps.executeQuery()) {
                if (rs.next()) {
                    User user = new User();
                    user.setId(rs.getString("id"));
                    user.setName(rs.getString("name"));
                    user.setPassword(rs.getString("password"));
                    return user;
                } else {
                    return null; // ID에 해당하는 사용자가 없는 경우
                }
            }
        }
    }
}
