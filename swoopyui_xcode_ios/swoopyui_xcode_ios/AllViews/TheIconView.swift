//
//  TheIconView.swift
//  swoopyui
//
//  Created by Yousif Aladwani on 09/08/2023.
//

import SwiftUI

struct TheIconView: View {
    @State var host_port : Int
    @State var textData : SwoopyView
    var body: some View {
        Image(systemName: "\(textData.image_name!)")
            .resizable()
            .frame(width: CGFloat(textData.width ?? 15), height: CGFloat(textData.height ?? 15))
            .foregroundColor(getColorFromString(colorName: textData.fgcolor!))
    }
}
