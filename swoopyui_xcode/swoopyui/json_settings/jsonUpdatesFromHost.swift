struct Update : Codable {
    var update_number : Int?
    var action : ActionUpdate?
}

struct ActionUpdate : Codable{
    var name : String
    var content : ActionUpdateContent
}

struct ActionUpdateContent : Codable {
    var empty : Bool?
    var error_describe : String?
    var new_view_content : SwoopyView?
    var view_id : Int?
}

struct SwoopyView : Codable, Equatable {
    var last_view_id : Int?
    var view_id : Int
    var vname : String
    var text : String?
    var title : String?
    var placeholder : String?
    var fgcolor : String?
    var bgcolor : String?
    var width : Float?
    var height : Float?
    var sub_views : [SwoopyView]?
    var stack_type : String?
    var bold : Bool?
    var size : Float?
    var scroll_to_view_id : Int?
    var scroll_mode : String?
    var image_name : String?
    var scall_to_fit : Bool?
    var value : String?
    var resizeable : Bool?
}
